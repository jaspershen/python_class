DEFINE-NEW-INSTRUCTION turnright AS
  BEGIN
    turnleft turnleft turnleft   # three lefts equal a right
  END

# loading beepers

move ITERATE 9 TIMES pickbeeper
move ITERATE 9 TIMES pickbeeper
move ITERATE 9 TIMES pickbeeper
move ITERATE 9 TIMES pickbeeper
move ITERATE 9 TIMES pickbeeper
move ITERATE 9 TIMES pickbeeper
move ITERATE 9 TIMES pickbeeper

# return to starting position
turnleft turnleft move move move move move turnleft turnleft

# start design

WHILE any-beepers-in-beeper-bag DO
  BEGIN
    IF front-is-clear THEN
      BEGIN

# logic to turn or go forward

      END
    ELSE
      turnoff
  END
