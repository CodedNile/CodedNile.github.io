---
date:
  created: 2025-06-29

categories:
  - Dart
tags:
  - Dart
  - Programming language
authors:
  - poula
---

# Control Statement

<!-- more -->

## Control Statement

```bash

(if-else)

if(condition){

code if condition true

}else {

code if condition false

}
```

### 1- Check The Number

```dart

void main(){
// 1- num
// 2- check even or odd
// 3- even
// 4- odd
int num = int.parse(stdin.readLineSync()!);
if(num % 2 == 0){ // 10 / 2 = 5 true
print("num is Even");
}else { // 9 / 2 = 4.5 false
print("num is Odd");
}
}
```


### 2-Grades

```dart

void main (){  
//85 - 100 -> Excellent  
//75 - 85 ->  Very Good  
//65 - 75 -> Good  
//50 - 65 -> Pass  
// < 50 -> Failed  
  
  int grade = int.parse(stdin.readLineSync()!);  
  if (grade >= 85 && grade <= 100){  
    print("Excellent");  
  }else if(grade >= 75 && grade < 85){  
    print("Very Good");  
  }else if(grade >= 65 && grade < 75){  
    print("Good");  
  }else if(grade >=50 && grade < 65){  
    print("Pass");  
  }else {  
    print("Failed");  
  }  
}
```
### 3-Calculate the Max and Min
```dart
import 'dart:io';

void main() {
  print("Please enter your num1:");
  int num1 = int.parse(stdin.readLineSync()!);

  print("Please enter your num2:");
  int num2 = int.parse(stdin.readLineSync()!);

  print("Please enter your num3:");
  int num3 = int.parse(stdin.readLineSync()!);

  if (num1 > num2 && num1 > num3) {
    print("$num1 is the max");
    if (num2 < num3) {
      print("$num2 is the min");
    } else {
      print("$num3 is the min");
    }
  } else if (num2 > num1 && num2 > num3) {
    print("$num2 is the max");
    if (num1 < num3) {
      print("$num1 is the min");
    } else {
      print("$num3 is the min");
    }
  } else {
    print("$num3 is the max");
    if (num1 < num2) {
      print("$num1 is the min");
    } else {
      print("$num2 is the min");
    }
  }
}
```
