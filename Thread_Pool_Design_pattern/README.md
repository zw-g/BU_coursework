# Thread Pool Design pattern

Provide a description of the application use case scenario that you have selected for your final
project.

    I have design an example for Thread Pool Design Pattern.
    Thread Pool is like worker, so I imagined them as the cashier for a supermarket.
    so I have designed the program around the idea of supermarket.

    In order for the super market check out counter to work I need a shopping list, I create another
    thread name cusomter they will create a lot of shopping list for us to work with.
    
    When I was learning advance programming I love the idea thread use the full potential of yor 
    processors so I have choose to design the system for supermarket, using Thread Pool.

    Use case scenario:
    This application could be used for online shopping, especially during holiday times, when they
    require a lot computational power thread pool can use all of the computational power to achieve
    the calculation.
    if there is a million people submit for a order, the processing time for one order might not be
    a lot but if there is a million checkout request this application will come in handy to handle
    miltiple transactions at the same time.

Describe what are your main software design concepts regarding this application. For example
describe:

    • What are the design goals in your project?
    In this project I hope I code design something that is easy for student to study from it, 
    if they want to learn about Thread Pool design pattern. so I try to make everything clear.

    • How is the flexibility, of your implementation, e.g., how you add or remove in future new types?
    Thread pool its a pretty easy design pattern you just have to learn the right to build it.
    in term of flexibility you could imagine Cashier class is the worker class, and worker could do anything
    so if you would like you worker to do somehting else you will just have to add another object
    and make them work that object

    • How is the simplicity and understandability of your implementation?
    My goal for this project is to help people learn about Design patterns - Thread Pool
    so I have tried to make everything as clear as possible, there are not a lot of classes
    and I have added a lot of inline comments, so I think my project is having a very good
    understandability and simplicity.

    • How you avoided duplicated code?
    I have tried to reuse the same local variable, and within the same classs I have created method
    that could be used over and other again. I also extract method and pull up for subclasses of 
    the same hierarchy. try to use obejct for differenct classes.

# How to compile the project

We use Apache Maven to compile and run this project.

You need to install Apache Maven (https://maven.apache.org/)  on your system.

Type on the command line:

```bash
mvn clean compile
```

# How to create a binary runnable package

```bash
mvn clean compile assembly:single
```

# How to run

```bash
mvn -q clean compile exec:java -Dexec.executable="edu.bu.met.cs665.Main" -Dlog4j.configuration="file:log4j.properties"
```

We recommand the above command for running the Main Java executable.

# Run all the unit test classes.

```bash
mvn clean compile test checkstyle:check  spotbugs:check
```

# Using Spotbugs to find bugs in your project

To see bug detail using the Findbugs GUI, use the following command "mvn findbugs:gui"

Or you can create a XML report by using

```bash
mvn spotbugs:gui 
```

or

```bash
mvn spotbugs:spotbugs
```

```bash
mvn spotbugs:check 
```

check goal runs analysis like spotbugs goal, and make the build failed if it found any bugs.

For more info see
https://spotbugs.readthedocs.io/en/latest/maven.html

SpotBugs https://spotbugs.github.io/ is the spiritual successor of FindBugs.

# Run Checkstyle

CheckStyle code styling configuration files are in config/ directory. Maven checkstyle plugin is set
to use google code style. You can change it to other styles like sun checkstyle.

To analyze this example using CheckStyle run

```bash
mvn checkstyle:check
```

This will generate a report in XML format

```bash
target/checkstyle-checker.xml
target/checkstyle-result.xml
```

and the following command will generate a report in HTML format that you can open it using a Web
browser.

```bash
mvn checkstyle:checkstyle
```

```bash
target/site/checkstyle.html
```




