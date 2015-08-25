fact <- function(x) {
  if (x == 1) return(x)
  else return(x * fact(x - 1))
}

absolute <- function(x) {
  return(x * ((x < 0) * -1 + (x > 0)))
}

cosTaylor <- function(x) {
  result <- 1; i <- 2; step <- 1
  
  while(TRUE) {
    if (step %% 2 == 0) {
      term <- x^i/fact(i)
    } else {
      term <- x^i/fact(i) * -1
    }
    
    if (absolute(term) < 0.000001) break
    
    result <- result + term
    i <- i + 2
    step <- step + 1
  }
  
  return(result)
}

dottie <- function(number) {
  last <- number
  number <- cosTaylor(number)
  if (absolute(last - number) < 0.000001) {
    return(number)
  } else {
    return(dottie(number))
  }
}
  
> dottie(5)
0.7390855
> dottie(30)
0.7390855