var countBits = function(n) {
  
    let checker = n; // Sets the checker variable to the incoming argument number
    
    let binary_digits = []; // Creates an empty array
    
    let sum = 0; // The final value that will be returned

    let remainder = 0; // This will be a bit value of 0 or 1. When it is 2, the nubmer is converted. 

    const counter = 1; // A variable used to increment down. Not needed. You are supposed to divide by 2. 

    while (checker > 0)
    {
        remainder = checker % 2; // Create a remainder value.
        binary_digits.unshift(remainder); // Add the binary value to the FRONT of the array.
        checker = floor(checker / 2);
    }

    
    for (let i = 0; i < binary_digits.length; i++) {
      sum += binary_digits[i];
    }
    
    return sum;
    //First take the integer n and convert it into binary
    
    // How do you do that? You can take the integer and % 2 it. This gives a remainder.
    
    // Add the remainders to an array. 
    
    // Sum up the array? Return that value. 
    
  };