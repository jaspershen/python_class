DEFINE-NEW-INSTRUCTION turnright AS
  BEGIN
    turnleft turnleft turnleft # three lefts equals a turnright
  END

BEGIN
  move
  turnright
  ITERATE 2 TIMES move
  move
  turnright
  move

  ITERATE 5 TIMES move
END
