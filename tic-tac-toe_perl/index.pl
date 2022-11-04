#!/usr/bin/env perl

use strict;
use warnings;
use 5.010;

use Scalar::Util qw(looks_like_number);

my @a  = ( " ", " ", " ", " ", " ", " ", " ", " ", " " );

my @b = (
	"                      \n",
	"          |     |     \n",
	"       " . $a[0] . "  |  " . $a[1] . "  |  " . $a[2] . "      \n",
	"          |     |     \n",
	"     -----+-----+-----\n",
	"          |     |     \n",
        "       " . $a[3] . "  |  " . $a[4] . "  |  " . $a[5] . "      \n",
        "          |     |     \n",		
	"     -----+-----+-----\n",
        "          |     |     \n",
        "       " . $a[6] . "  |  " . $a[7] . "  |  " . $a[8] . "      \n",
        "          |     |     \n",
	"                      \n",
	"     Player: ",
);

my @c = ( "X", "O" );

while (1) {

	foreach my $d (@b) { print $d; }

	chomp (my $e = <>);
	my $f = length $e;
	print "\n";

	if ($f == 1) {
		my $isnum = looks_like_number( $e );
		# print "Print " . $isnum;
		if ($isnum) {
			my $g = int($e);
			if (($g >= 0) and ($g <= 8)) {
				$a[$g] = "X";
				print $a[$g] .  " my measurement so far";
				for (my $h=0; $h<9; $h++) {
					print $a[$h] . " ";
				}
				if ($g == 8) {
					last;
				}

			} else {
				next;
			}
		} else {
			next;
		}
	} else {
		next;
	}	
}

