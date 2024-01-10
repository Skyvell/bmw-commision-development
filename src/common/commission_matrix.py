class CommissionResult:
    def __init__(self, elegible: bool, commission: float):
        self.eligible = elegible
        self.commission = commission

class CommissionMatrix:
    def __init__(self, json):
        self.matrix = json['matrix']
        self.x_axis = json['x-axis']
        self.y_axis = json['y-axis']
    
    def get_commission(self, penetration_rate: float, target_volume_achieved: float):
        if not self._is_eligible_for_commission(penetration_rate, target_volume_achieved):
            return CommissionResult(False, 0)
        
        commission = self.matrix[self._find_row_index(penetration_rate)][self._find_column_index(target_volume_achieved)]
        return CommissionResult(True, commission)

    def _find_row_index(self, penetration_rate: float) -> int:
        for i in range(len(self.y_axis) - 1):
            if self.y_axis[i] <= penetration_rate < self.y_axis[i + 1]:
                return len(self.y_axis) -1 - i 
        
        return 0
            
    def _find_column_index(self, target_volume_achieved: float) -> int:
        for i in range(len(self.x_axis) - 1):
            if self.x_axis[i] <= target_volume_achieved < self.x_axis[i + 1]:
                return i
            
        return i + 1
          
    def _is_eligible_for_commission(self, penetration_rate: float, target_volume_achieved: float) -> bool:
        if penetration_rate < self.y_axis[0] or target_volume_achieved < self.x_axis[0]:
            return False
        else:
            return True
