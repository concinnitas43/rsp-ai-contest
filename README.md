# something

    hand: (r/p/s)

    match: (hand, hand)
        p1_hand, p2_hand (r/p/s)

        evalute( self ) -> 1, 0, -1 // 1 p1 wins, 0 tie, -1 p2 wins

    History: list[match]
        p1_hands, p2_hands list[(r/p/s)] 

    agent
        history: History 
        
        play( history, memo, * ) -> hand, memo

    game
        p1, p2: agent
        history: History // p1hands default flip for p2
        memo1, memo2: Memo

        play( self ):
            hand1, memo1 <- p1 play history, memo1
            hand2, memo2 <- p2 play history, memo2

            history append (hand1, hand2)

        evaluate( self ):
            sum eval history

        print, str, ...




