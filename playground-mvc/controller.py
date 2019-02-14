class MyController:
    def __init__(self, model, view):
        print("MyController::__init__(app, model, view)")

        self.model = model
        self.view = view
        self.model.controller = self
        self.view.controller = self
    def showData(self):
        #print(self.model.database.data)
        return self.view.getVal(self.model.database.data)
    def buttInc(self):
        if self.view.buttonClicked() == True:
            #self.model.database.data = self.model.database.data + 1
            #print(self.model.database.data)
            print("added 1")
            self.showData()
            #return self.view.getVal(self.model.database.data)
    def run(self):
        print("MyController::run()")
        self.buttInc()
        self.showData()
        self.view.run()
