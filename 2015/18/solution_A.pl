#!/usr/bin/perl
use warnings; use strict;

my $steps = $ARGV[0] or die "Number of steps is missing\n";

my @neighbors = (
  [-1, -1], [ 0, -1], [ 1, -1],
  [-1,  0],           [ 1,  0],
  [-1,  1], [ 0,  1], [ 1,  1],
);

my $map = [];
while (<STDIN>) {
  my @r = ();
  chomp;
  map { push @r, $_ eq '#' ? 1 : 0 } split '';
  push @$map, \@r;
}
my $max_y = $#$map;
my $max_x = $#{$map->[0]};
#print_grid($map);

for (1..$steps) {
  $map = step($map);
  #print_grid($map);
}
print count_on($map), "\n";

sub step {
  my $grid = shift;
  my @new = ();

  for (my $y = 0; $y <= $#$grid; $y++) {
    my @r = ();
    for (my $x = 0; $x <= $#{$grid->[$y]}; $x++) {
      my $on = 0;
      for my $n (@neighbors) {
        my $nx = $x + $n->[0];
        my $ny = $y + $n->[1];
        next if $nx < 0 or $ny < 0 or $nx > $max_x or $ny > $max_y;
        $on += $grid->[$ny]->[$nx];
      }
      $r[$x] = ($grid->[$y]->[$x] == 1 && ($on == 2 || $on == 3)) || ($grid->[$y]->[$x] == 0 && $on == 3) ? 1 : 0;
    }
    push @new, \@r;
  }

  return \@new;
}

sub count_on {
  my $g = shift;
  my $on = 0;

  for (my $y = 0; $y <= $#$g; $y++) {
    for (my $x = 0; $x <= $#{$g->[$y]}; $x++) {
      $on += $g->[$y]->[$x];
    }
  }

  return $on;
}

sub print_grid {
  my $g = shift;
  map { print join(' ', @$_), "\n" } @$g;
  print "\n";
}
