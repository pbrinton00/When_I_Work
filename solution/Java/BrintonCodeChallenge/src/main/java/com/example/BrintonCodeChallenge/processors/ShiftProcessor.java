package com.example.BrintonCodeChallenge.processors;

import com.example.BrintonCodeChallenge.vdo.ShiftDO;
import org.springframework.stereotype.Component;
import java.util.List;

@Component
public class ShiftProcessor {

    /**
     * Process a list of shifts
     * @param List of Shifts
     * @Return VOID
     */

    public void processShifts(List<ShiftDO> shifts){

        // Call validation service to verify data integrity

        // Call validation service to verify shift
        // If invalid push to resolution service and move to nest record
        // If valid continue

        // persist shift in data store

        // done
    }
}
