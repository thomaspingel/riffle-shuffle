function [shuffled] = riffle(deck,ntimes)

if nargin<2 ntimes=1; end
for k=1:ntimes
    
    % Size of deck
    n = length(deck);
    
    % Split the deck according to binomial distribution
    lastCard = binornd(n,.5);
    halfdeck{1} = deck(1:lastCard);
    halfdeck{2} = deck(lastCard+1:end);
    
    % Create the shuffled deck and fill with zeros
    shuffled = zeros(size(deck));
    
    
    % Do the riffle, with the probability of a card being dropped from each
    % half being proportional to the number of cards in it.

    for i=1:n
        
        % Find out which deck to take from
        deckToTakeFrom = 2;
        p=rand(1);
        if p<=(length(halfdeck{1})/(length(halfdeck{1})+length(halfdeck{2})))
            deckToTakeFrom=1;
        end
       
        shuffled(i) = halfdeck{deckToTakeFrom}(end);
        halfdeck{deckToTakeFrom}(end)=[];
    end
    shuffled=rot90(rot90(shuffled));
    deck=shuffled;
end