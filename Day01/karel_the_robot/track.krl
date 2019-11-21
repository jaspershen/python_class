DEFINE-NEW-INSTRUCTION turnright AS
  BEGIN
    turnleft turnleft turnleft
  END

DEFINE-NEW-INSTRUCTION check-for-beeper-right AS
    IF right-is-clear THEN
        BEGIN
          BEGIN
            turnright move
	        END
          IF next-to-a-beeper THEN
            pickbeeper
          ELSE
  	        BEGIN
              turnleft turnleft move turnright
  	        END
        END

DEFINE-NEW-INSTRUCTION check-for-beeper-left AS
    IF left-is-clear THEN
        BEGIN
          BEGIN
            turnleft move
	        END
          IF next-to-a-beeper THEN
            pickbeeper
          ELSE
            BEGIN
              turnleft turnleft move turnleft
	          END
	      END

DEFINE-NEW-INSTRUCTION find-beeper AS
    WHILE front-is-clear DO
      IF next-to-a-beeper THEN
        BEGIN
	        pickbeeper
          check-for-beeper-right
          check-for-beeper-left
	      END
      ELSE
        move

WHILE not-next-to-a-beeper DO
  BEGIN
    find-beeper
    IF front-is-blocked THEN
      turnoff
  END
