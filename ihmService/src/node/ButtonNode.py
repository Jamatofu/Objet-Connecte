from . import Tree

class ButtonNode(Tree.Tree):
    def __init__(self, buttonText, destination, name, value, autoreload="false", onchange="null"):
        super().__init__("button")
        self.buttonText = buttonText
        self.destination = destination
        self.name = name
        self.value = value
        self.autoreload = autoreload
        self.onchange = onchange

    def generate(self):
        checked = ""

        if (self.value == True):
            checked = "checked"

        return """
            <div>
                <span>{}</span>
                <label class="switch">
                  <input type="checkbox"  onclick="updateActionneur(this, '{}', '{}', '{}', '{}');
                    makeObjectInvisible(this.checked    , '{}')"
                    {}>
                  <span class="slider round"></span>
                </label>
            </div>
        """.format(self.buttonText,
                    self.destination,
                    self.value,
                    self.name,
                    self.autoreload,
                    self.onchange,
                    checked)
