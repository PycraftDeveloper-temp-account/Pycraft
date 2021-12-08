Nomanclature and programming techniques
=======

Pycraft maintains a scheme for naming variables and controlling code structure in Pycraft; this section details all the information you will need for understanding the structure for the program, in addition to the nomanclature (a series of rules that determines how objects should be named). This section will also help you understand the comments and documentation attached below, we strongly recommend you read this before getting started!

Some of these rules are NOT yet integrated into Pycraft, but wil be accommodated into versions of Pycraft greater than or equal to v0.9.4 (or v0.9.4-1 pre-release found here: https://github.com/PycraftDeveloper/Pycraft-Insider-Preview).

Variables
+++++++++

* All variables should be named in accordance to its function, or based on a description of the data it stores.
* There is no limit to the length of the name of a variable as at current there is no limit on the length of a line of code.
* Variables must also be preceeded by a data-type
Good examples of variable nomanclature include:
``int_StoresRandomNumber``
or
``vao_StoreMapVertexBuffer``

Procedures
+++++++

* Procedures can be of any length, as there is no limit to the length of a line of code in Pycraft at present.
* Procedures should avoid using global variables as much as possible, as this makes it easier to trace variables and possible bugs. (The exceptions here being the ``Class_Startup_variables`` and ``self`` variables which are referenced throughout the different modules for Pycraft).
* Procedures should be named according to their function, and not be dependant on other code in a spacific module to work. (For example, making a random number generator that relies on global variables created elsewhere in a module)
* Procedures should only have parameters if they are used withing the procedure.
* If a procedure returns a value, then this must be implicitly stated in the documentation here.

Modules
+++++++

* All modules should be preceeded by the following code, regardless of function:
 .. code-block:: python

if not __name__ == "__main__":
    print("Started <Pycraft_<name>>")
    class <name>:
        def __init__(self):
            pass
