# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

    def test_backstage_passes_increase_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)

        # Additional check for under 10 days left
        items[0].sell_in = 10
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)  # Increases by 2

        # Check for under 5 days left
        items[0].sell_in = 5
        gilded_rose.update_quality()
        self.assertEqual(26, items[0].quality)  # Increases by 3

        # Check after the concert
        items[0].sell_in = 0
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)  # Drops to 0

    def test_conjured_item_degradation(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)  # Degrades twice as fast
        self.assertEqual(2, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
