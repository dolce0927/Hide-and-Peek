"""
file: seeMeDont.py
author: Ro
"""

from breezypythongui import EasyFrame

class PeekABoo(EasyFrame):
	"""buttons and events"""

	def __init__(self):
		"""sets up the window, label, and buttons."""
		EasyFrame.__init__(self, width = 200, height = 200, title = "PeekABoo", background = "cyan")

		# A single label in the first row.
		self.see = self.addLabel(text = "Now You See Me", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "cyan")

		self.dont = self.addLabel(text = "", row = 1, column = 0, columnspan = 2, sticky = "NSEW", background = "cyan")

		self.clickBtn = self.addButton(text = "Click", row = 2, column = 0, command = self.click)
		
	# Methods to handle user events	
	def click(self):
		"""allows the two diff text lines to appear and disappear"""
		if self.see["text"] != "":
			self.dont["text"] = "Now You Dont!"
			self.see["text"] = ""
			self.dont["foreground"] = "blue"
		else:
			self.see["text"] = "Now You See Me Again"
			self.dont["text"] = ""

def main():
	"""Instantiates and pops up the window."""
	PeekABoo().mainloop()

if __name__ == "__main__":
	main()	
