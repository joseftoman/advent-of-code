#!/usr/bin/perl
use warnings; use strict;
use Data::Dump;

my %v;
my $buff = [];
my $round = 0;

for my $c (<STDIN>) {
  my $p = parse_command($c);
  push @$buff, $p if defined $p;
}
print "$round: ", scalar(@$buff), " left, ", scalar(keys %v), " set\n";

while (not exists $v{a}) {
  my $next = [];

  for my $c (@$buff) {
    my $set = 1;
    for (my $i = 0; $i <= $#{$c->[0]}; $i++) {
      next if $c->[0]->[$i];
      if (exists $v{$c->[1]->[$i]}) {
        $c->[1]->[$i] = $v{$c->[1]->[$i]};
        $c->[0]->[$i] = 1;
      } else {
        $set = 0;
      }
    }

    if ($set) {
      if ($c->[2] eq 'NOT') {
        $v{$c->[3]} = ~$c->[1]->[0] & 65535;
      } elsif ($c->[2] eq 'AND') {
        $v{$c->[3]} = $c->[1]->[0] & $c->[1]->[1];
      } elsif ($c->[2] eq 'OR') {
        $v{$c->[3]} = $c->[1]->[0] | $c->[1]->[1];
      } elsif ($c->[2] eq 'LSHIFT') {
        $v{$c->[3]} = $c->[1]->[0] << $c->[1]->[1];
      } elsif ($c->[2] eq 'RSHIFT') {
        $v{$c->[3]} = $c->[1]->[0] >> $c->[1]->[1];
      } elsif ($c->[2] eq 'SET') {
        $v{$c->[3]} = $c->[1]->[0];
      } else {
        print "ERROR: unknown gate '$c->[2]'\n";
      }
    } else {
      push @$next, $c;
    }
  }

  $buff = $next;
  $round++;
  print "$round: ", scalar(@$buff), " left, ", scalar(keys %v), " set\n";
  last if $round == 150;
}

print "$v{a}\n" if exists $v{a};

sub parse_command {
  my $c = shift;
  my @p;
  my ($o1, $o2, $g, $d);

  if (($o1, $d) = $c =~ m/^(\w+) -> ([a-z]+)$/) {
    if ($o1 =~ m/^\d+$/) {
      $v{$d} = int($o1);
      return;
    } else {
      return [ [0], [$o1], 'SET', $d ];
    }
  } elsif (($o1, $g, $o2, $d) = $c =~ m/^(\w+) ((?:L|R)SHIFT|AND|OR) (\w+) -> ([a-z]+)$/) {
    @p = ([], [$o1, $o2], $g, $d);
  } elsif (($o1, $d) = $c =~ m/^NOT (\w+) -> ([a-z]+)$/) {
    @p = ([], [$o1], 'NOT', $d);
  } else {
    print "PARSE ERROR: $c\n";
  }

  for (my $i = 0; $i <= $#{$p[1]}; $i++) {
    if ($p[1]->[$i] =~ m/^\d+$/) {
      $p[1]->[$i] = int($p[1]->[$i]);
      $p[0]->[$i] = 1;
    } else {
      $p[0]->[$i] = 0;
    }
  }

  return \@p;
}
