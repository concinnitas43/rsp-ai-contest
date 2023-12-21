# something

    hand: (r/p/s)

    match: (hand, hand)
        p1_hand, p2_hand (r/p/s)

        evalute( self ) -> 1, 0, -1 // 1 p1 wins, 0 tie, -1 p2 wins

    History: list[match]
        p1_hands, p2_hands list[(r/p/s)] 

    agent
        play( history, memo, * ) -> hand, memo

    game
        p1, p2: agent
        history: History // p1hands default flip for p2

        play( self ):
            hand1<- p1 play history
            hand2<- p2 play history

            history append (hand1, hand2)

        evaluate( self ):
            sum eval history

        print, str, ...




