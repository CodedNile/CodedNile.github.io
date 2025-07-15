---
date:
  created: 2025-07-15

categories:
  - Answer
tags:
  - Dart
  - Answer
authors:
  - poula
---

# Control Statement (Answer)

<!-- more -->

## Control Statement (Answer)

## Exercise 1

Create a program that asks the user to enter their name and their age. Print out a message that tells how many years they have to be 100 years old.

```dart
import 'dart:io';

void main() {
  print("What's your name? ");
  String name = stdin.readLineSync()!;
  print("Hi, $name What is your age?");
  int age = int.parse(stdin.readLineSync()!);
  int calc = 100 - age;
  print("CodedNile, You have $calc years to be 100");
}
/// name String
/// age int
/// calc int
```

## Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

```dart
import 'dart:io';

void main() {
  print("Hi, please choose a number: ");
  int num = int.parse(stdin.readLineSync()!);
  if (num % 2 == 0) { // 10 / 2 (2 2 2 2 2)  0
    print("$num is even");
  } else { // 9 / 2 (2 2 2 2 1)
     print("$num is odd");
  }
}
/// num int
```

## Exercise 3

Write a program to check whether an alphabet is a vowel or consonant.
Vowel alphabet is ( ‫المتحركه‬ ‫الحروف‬ ):(a,i,o,u,e)
Consonant : rest of alphabets

```dart
import 'dart:io';

void main() {
  print("Please Enter your Character");
  String char = stdin.readLineSync()!;
  if (char == "a" || char == "i" || char == "o"|| char == "e" || char == "u") {
    print("$char is vowel");
  } else {
    print("$char is constant");
  }
}
// a i o u e
```

## Exercise 4

Write a program that prompts the user to enter the grade for student and show up a
message for him
1-if he gets A write Excellent
2-if he gets B write Outstanding
3- if he gets C write Good
4-if he gets D write Can Do Better
5- if he gets F write Failed !
if user entered another grade write invalid grade

```dart
import 'dart:io';

void main() {
  print("Please enter your garde?");
  String grade = stdin.readLineSync()!;
  if (grade == 'a') {
    print("Excellent");
  } else if (grade == 'b') {
     print("Outstanding");
  }else if (grade == 'c') {
     print("Good");
  }else if (grade == 'd') {
     print("Can Do Better");
  }else if (grade == 'f') {
     print("Failed");
  }
}


///1-if he gets A write Excellent
///2-if he gets B write Outstanding
///3- if he gets C write Good
///4-if he gets D write Can Do Better
/// 5- if he gets F write Failed
```

## Exercise 5

Write a program that reads in the radius
and length of a cylinder and computes the area and volume using the following
formulas:

area = radius _ radius _ pi

volume = area \* length

```dart
import 'dart:io';

void main() {
  print("Enter the radius and length of a cylinder:");
  double radius = double.parse(stdin.readLineSync()!);
  double length = double.parse(stdin.readLineSync()!);
  double area = radius * radius * 3.14159265359;
  double volume = area * length;
  print("The area is $area");
  print("The volume is $volume");
}
/// radius
/// length
/// area
/// volume
///
```

## Exercise 6

Write a program that prompts the user to enter an integer
and check if this number is negative or zero or positive show up a massage with its
sign

```dart
import 'dart:io';

void main() {
  print("Please Enter Your Number");
  int num = int.parse(stdin.readLineSync()!);
  if (num > 0) {
    print("$num is positive");
  } else if (num < 0) {
    print("$num is negative");
  } else if (num == 0) {
    print("num is zero");
  }
}

/// positive
/// negative
/// zero

```

## Exercise 7

How can you find the minimum/maximum of three numbers using if.

```dart
import 'dart:io';

void main() {
  print("Please enter your num1");
  int num1 = int.parse(stdin.readLineSync()!);
  print("Please enter your num2");
  int num2 = int.parse(stdin.readLineSync()!);
  print("Please enter your num3");
  int num3 = int.parse(stdin.readLineSync()!);

  if (num1 > num2 && num1 > num3) {
    print("$num1 is max");
    if (num2 < num3) {
      print("$num2 is min");
    } else {
      print("$num3 is min");
    }
  } else if (num2 > num3 && num2 > num1) {
    print("$num2 is max");
    if (num3 < num1) {
      print("$num3 is min");
    } else {
      print("$num1 is min");
    }
  } else if (num3 > num1 && num3 > num2) {
    print("$num3 is max");
    if (num1 < num2) {
      print("$num1 is min");
    } else {
      print("$num2 is min");
    }
  }
}

```

## Exercise 8

Write a program to input cost price and selling price of a product and check profit or loss. Also calculate total profit or loss using if else. How to calculate profit or loss on any product using if else .

```dart
import 'dart:io';

void main() {
  print("Enter cost price:");
  int cost = int.parse(stdin.readLineSync()!);
  print("Enter selling price:");
  int selling = int.parse(stdin.readLineSync()!);
  int calc = selling - cost;
  if (selling > cost) {
    print("profit is $calc");
  } else if (selling < cost) {
    print("loss is $calc");
  }
}

```
