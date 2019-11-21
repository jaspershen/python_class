DEFINE-NEW-INSTRUCTION turnright AS
  BEGIN
    turnleft turnleft turnleft   # a comment
  END

DEFINE-NEW-INSTRUCTION stayright AS
  BEGIN
    IF XXX-is-clear THEN
      BEGIN
        turnXXX
        move
      END
    ELSE
      BEGIN
        IF XXX-is-clear THEN
          move
        ELSE
          IF XXX-is-clear THEN
            turnXXX
          ELSE
            turnoff
      END
  END

ITERATE 75 TIMES stayright
