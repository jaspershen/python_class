DEFINE-NEW-INSTRUCTION movebeepers AS
  BEGIN
    IF next-to-a-beeper THEN pickbeeper
      ITERATE 4 TIMES move
      IF any-beepers-in-beeper-bag THEN putbeeper ITERATE 2 TIMES turnleft
      ITERATE 4 TIMES move
      ITERATE 2 TIMES turnleft
  END

DEFINE-NEW-INSTRUCTION findbeepers AS
  BEGIN
    WHILE not-next-to-a-beeper DO
      BEGIN
        move
      END
  END

WHILE not-facing-west DO
  BEGIN
    turnleft
  END

findbeepers

WHILE next-to-a-beeper DO
  BEGIN
    movebeepers
  END

turnoff
