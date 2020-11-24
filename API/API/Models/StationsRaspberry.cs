using System;
using System.Collections.Generic;

namespace GeoLabAPI
{
    public partial class Raspberry
    {
        public int Id { get; set; }
        public int RaspberryId { get; set; }
        public double? latitude { get; set; }
        public double? longitude { get; set; }

        public Raspberry()
        {
            
        }

        public Raspberry(int raspberryID, double? lat, double? lon)
        {
            RaspberryId = raspberryID;
            latitude = lat;
            longitude = lon;
        }
    }
}
