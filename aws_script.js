printClosest([3317.64, 2424.72, 13535.4, 3317.64, 4859.04, 20701.2, 5522.72, 8098.4, 11146.8, 1546.632, 23796.32, 2981.36, 1546.632, 17041.28, 34080.56, 4247.68, 27215.76, 13845.72, 38686.08, 51123.84, 153371.52, 102241.68, 14866.88, 17615.312, 27757.492, 8520.64, 11570.4, 2123.84, 22267.44, 29669.4, 70118.52, 170402.8, 12743.04, 8547.92, 7447.132, 14866.88, 4273.96, 12370.8, 29669.4, 9671.52, 102247.68, 136322.24, 31857.6, 8547.92, 47425.84, 13540.24, 24590.12], 778592.81);


function printClosest(array, value, limit) {
  var checkLength = function(array) {
    return array.length === limit;
  };
  var combinations = combine(array); //get all combinations
  combinations = limit ? combinations.filter(checkLength) : combinations;//limit length if required
  var sum = combinations.map(function(c) { //create an array with sum of combinations
    return c.reduce(function(p, c) {
      return p + c;
    }, 0)
  });
  var sumSorted = sum.slice(0).sort(function(a, b) {//sort sum array
    return a - b;
  });

  index = locationOf(value, sumSorted);//find where the value fits in
  index = (Math.abs(value - sum[index]) <= Math.abs(value - sum[index + 1])) ? index : index + 1;
  index = index >= sum.length ? sum.length - 1 : index;
  index = sum.indexOf(sumSorted[index]);//get the respective combination

  //console.log(sum, combinations, index);

  console.log(value, combinations[index].toString(), limit);
}


function combine(a) {
  var fn = function(n, src, got, all) {
    if (n == 0) {
      if (got.length > 0) {
        all[all.length] = got;
      }
      return;
    }
    for (var j = 0; j < src.length; j++) {
      fn(n - 1, src.slice(j + 1), got.concat([src[j]]), all);
    }
    return;
  }
  var all = [];
  for (var i = 0; i < a.length; i++) {
    fn(i, a, [], all);
  }
  all.push(a);
  return all;
}

function locationOf(element, array, start, end) {
  start = start || 0;
  end = end || array.length;
  var pivot = parseInt(start + (end - start) / 2, 10);
  if (end - start <= 1 || array[pivot] === element) return pivot;
  if (array[pivot] < element) {
    return locationOf(element, array, pivot, end);
  } else {
    return locationOf(element, array, start, pivot);
  }
}
