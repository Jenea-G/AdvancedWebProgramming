Part 7 — Reflection Questions
Answer these briefly.

1. What is the difference between a constant and an enum?
   Constant has one fixed value that shouldn't be changed, while enum is a list of a number of possible values.

2. Why are enums safer than random strings?
   Random strings can cause bugs as every time we use/type them the risk of typos rises.

3. Why is CourseStatus.OPEN better than "open"?
   because we can reuse stored value as many times as we need and use it as a reference avoiding spelling mistakes.

4. Why did you use a property for status?
   I used a property to set it as a private attribute and impose a validation rule but still be able to access it as a property without creating a dedicated method to access this as a private attribute. In other words I could use a private attribute to protect it from random changes and then I would need to create specific methods to access and change this attribute (as it will be encapsulated), and would need to remember thouse specific methods names, thus creating a property simplifies it and I use just the property name to easily get or safely change its value.

5. How do enums help validation in class design?
   Enums help us avoid spelling differences and limit a class attribute to a fixed set of values.
