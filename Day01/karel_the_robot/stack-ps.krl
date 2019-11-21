DEFINE-NEW-INSTRUCTION findbeepers AS
  BEGIN
    WHILE not-next-to-a-beeper DO
#
# add code here
#
  END

WHILE not-facing-west DO
  BEGIN
    turnleft
  END

WHILE facing-west DO
  BEGIN
     findbeepers
     pickbeeper move move move move putbeeper
     turnleft turnleft
     ITERATE 7 TIMES move
     turnleft turnleft
  END
turnoff

