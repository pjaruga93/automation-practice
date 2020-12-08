@filter
Feature: Filtering products

  @filter_by_size
  Scenario Outline: Filter products by size
    Given I am on automationpractice page
     When I go to womens products view
      And I filter those products by size "<size>"
     Then Visible products should be in "<size>" size

    Examples:
    | size |
    | S    |
    | M    |
    | L    |


  @filter_by_color
  Scenario Outline: Filter products by color
    Given I am on automationpractice page
     When I go to womens products view
      And I filter those products by color "<color>"
     Then Visible products should be in "<color>" color

    Examples:
    | color  |
    | Beige  |
    | Black  |
    | Blue   |
    | Yellow |
    | White  |
    | Orange |
    | Green  |
    | Pink   |
