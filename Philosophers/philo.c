#include <pthread.h> 
#include <semaphore.h> 
#include <stdio.h> 
#include <unistd.h>
#define N 7  
#define RESTING 2 
#define EATING 1 
#define THINKING 0 
#define LEFT (currentPhilo + 6) % N 
#define RIGHT (currentPhilo + 1) % N 

int state[N]; 
int phil[N] = { 0, 1, 2, 3, 4, 5, 6 }; 

sem_t mutex; 
sem_t S[N]; 
void checking(int currentPhilo) 
{ 
	if (state[currentPhilo] == THINKING 
		&& (state[LEFT] != EATING 
		|| state[RIGHT] != EATING)) { 


		if (state[LEFT] != EATING )
		{
			printf("Philosopher %d takes chopstick %d \n", currentPhilo + 1, LEFT + 1);
			sleep(1.2);
			if (state[RIGHT] != EATING)
				{
				printf("Philosopher %d is Eating\n", currentPhilo + 1);
				printf("Philosopher %d takes chopsticks %d and %d\n", currentPhilo + 1, LEFT + 1, currentPhilo + 1);
				state[currentPhilo] = EATING; 	
				sem_post(&S[currentPhilo]); 
				sleep(1.2);	
				state[currentPhilo] = RESTING;
				printf("Philosopher %d is Resting\n\n", currentPhilo + 1);	 			
				}

		} 
		else if (state[RIGHT] != EATING )
		{	
			printf("Philosopher %d takes chopstick %d\n", currentPhilo + 1, currentPhilo + 1);
			if (state[LEFT] != EATING)
				{
				printf("Philosopher %d is Eating\n", currentPhilo + 1);
				printf("Philosopher %d takes chopsticks %d and %d\n", currentPhilo + 1, LEFT + 1, currentPhilo + 1);
				state[currentPhilo] = EATING; 
				sem_post(&S[currentPhilo]); 
				sleep(1.2);
				state[currentPhilo] = RESTING; 	
				printf("Philosopher %d is Resting\n", currentPhilo + 1);		
				}
			 

		}		
	}else if (state[currentPhilo] == RESTING && (state[LEFT] == THINKING 
		|| state[RIGHT] == THINKING))
		{
			state[currentPhilo] = THINKING;
			sem_post(&S[currentPhilo]);
			sleep(1.2);
		}else{
			state[currentPhilo] = EATING;
			sem_post(&S[currentPhilo]);
			sleep(1.2);
			}
}
		

void take_chopstick(int currentPhilo) 
{ 
	sem_wait(&mutex); 

	// state that hungry 
	state[currentPhilo] = THINKING; 

	printf("Philosopher %d is thinking\n", currentPhilo + 1); 

	// eat if neighbours are not eating 
	checking(currentPhilo); 

	sem_post(&mutex); 

	// if unable to eat wait to be signalled 
	sem_wait(&S[currentPhilo]); 

	sleep(1); 
} 

void put_chopstick(int currentPhilo) 
{ 
	sem_wait(&mutex); 

	// state that thinking 
	state[currentPhilo] = THINKING; 

	printf("Philosopher %d putting chopstick %d and %d down\n", 
		currentPhilo + 1, LEFT + 1, currentPhilo + 1); 
	printf("Philosopher %d is resting\n", currentPhilo + 1); 

	checking(LEFT); 

	checking(RIGHT); 

	sem_post(&mutex); 
}
void* philospher(void* num) 
{ 

	while (1) { 

		int* i = num; 

		sleep(1); 

		take_chopstick(*i); 

		sleep(0); 

		put_chopstick(*i); 
	} 
}
int main() 
{ 	int i; 
	pthread_t thread_id[N]; 

	// initialize the semaphores 
	sem_init(&mutex, 0, 1); 

	for (i = 0; i < N; i++) 

		sem_init(&S[i], 0, 0); 

	for (i = 0; i < N; i++) { 

		// create philosopher processes 
		pthread_create(&thread_id[i], NULL, 
					philospher, &phil[i]); 
		

		//printf("Philosopher %d is thinking\n", i + 1); 
	} 

	for (i = 0; i < N; i++) 

		pthread_join(thread_id[i], NULL); 
} 


