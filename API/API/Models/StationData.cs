using System;

namespace GeoLabAPI
{
    public partial class StationData
    {
        public int WEEK { get; set; }
        public double T { get; set; }
        public double AX { get; set; }
        public double AY { get; set; }
        public double AZ { get; set; }
        public double? Temp { get; set; }
        public int? Hour { get; set; }
    }
}
