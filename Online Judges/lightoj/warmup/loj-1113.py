
import sys
import os

LOCAL_ENV: bool = os.environ.get('USER') == 'trifiasco'

class Browser:
    """
    Responsible for simulating the browser behavior.
    
    Implement the methods as described in the problem.  
    """
    
    # Class variable to keep the default page loaded in the browser
    DEFAULT_PAGE = 'http://www.lightoj.com/'
    
    def __init__(self):
        """
        Initialize your data structures. If needed, keep the DEFAULT page as the initial page.
        """
        # Initialize your data structures
        self.backpages = [];
        self.frontpages = [];
        self.backpages.append(self.DEFAULT_PAGE)

    def back(self) -> str:
        """
        If the backward stack is empty, return 'Ignored'.
        
        Otherwise, push the current page on the top of the forward stack. Also
        Pop the page from the top of the backward stack, making it the new current page.
        
        return the new current page.
        """
        # Implement the above logic
        if len(self.backpages) == 1:
            return 'Ignored'

        currentPage = self.backpages.pop();
        self.frontpages.append(currentPage);
        return self.backpages[len(self.backpages) - 1];

        
    def forward(self) -> str:
        """
        If the forward stack is empty, return 'Ignored'.
         
        Otherwise, push the current page on the top of the backward stack. Also
        Pop the page from the top of the forward stack, making it the new current page.
         
        return the new current page.
        """
        # Implement the above logic
        if len(self.frontpages) == 0:
            return 'Ignored'

        currentPage = self.frontpages.pop();
        self.backpages.append(currentPage);
        return currentPage;
        
    def visit(self, url: str) -> str:
        """
        Push the current page on the top of the backward stack, and
        make the 'url' specified the new current page.
        
        The forward stack is also emptied.
        
        return the new current page.
        """
        # Implement the above logic
        self.backpages.append(url);
        self.frontpages.clear();
        return url

def solve():
    """
    Takes care of input and output.
    
    You don't have to make any changes here.
    """
    
    cases = int(input())
    for caseno in range(1, cases + 1):
        print('Case {}:'.format(caseno))
        
        browser = Browser()
        while True:
            command = input()
            if command == 'QUIT':
                break
            if command == 'BACK':
                print(browser.back())
            elif command == 'FORWARD':
                print(browser.forward())
            else:  # VISIT url
                _, url = command.split(' ', 2)
                print(browser.visit(url))


def READ():
    sys.stdin = open('in.txt', 'r');
    #sys.stdout = open('out.txt', 'w');

if __name__ == "__main__":
    if LOCAL_ENV:
        READ()
    solve()
    # while True:
        # try:
            # n = int(input())
            # # do stuff
        # except EOFError:
            # break
    pass
