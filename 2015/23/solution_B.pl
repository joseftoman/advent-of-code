#!/usr/bin/perl
use warnings; use strict;

my @prg = map { chomp; my @a = m/^(...) ([^,]+)(?:, (.*))?$/; [ grep defined($_), @a ] } <STDIN>;
my $pos = 0;
my %reg = (a => 1, b => 0);

while ($pos <= $#prg) {
  my $i = $prg[$pos]->[0];

  if ($i eq 'hlf') {
    $reg{$prg[$pos]->[1]} = $reg{$prg[$pos]->[1]} >> 1;
    $pos++;
  } elsif ($i eq 'tpl') {
    $reg{$prg[$pos]->[1]} *= 3;
    $pos++;
  } elsif ($i eq 'inc') {
    $reg{$prg[$pos]->[1]}++;
    $pos++;
  } elsif ($i eq 'jmp') {
    $pos += int($prg[$pos]->[1]);
  } elsif ($i eq 'jie') {
    if ($reg{$prg[$pos]->[1]} % 2 == 0) {
      $pos += int($prg[$pos]->[2]);
    } else {
      $pos++;
    }
  } elsif ($i eq 'jio') {
    if ($reg{$prg[$pos]->[1]} == 1) {
      $pos += int($prg[$pos]->[2]);
    } else {
      $pos++;
    }
  } else {
    die "Unknown instruction '$i'.\n";
  }
}

print "a = $reg{a}\nb = $reg{b}\n";
