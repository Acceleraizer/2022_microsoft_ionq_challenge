using UnityEditor;
using UnityEditor.Scripting.Python;
using UnityEngine;
using System;
using System.Collections;

public class CallingPython : MonoBehaviour
{
    public string gate_translate(int index) {
        if (index == 0) return "X";
        if (index == 1) return "H";
        if (index == 2) return "S";
        if (index == 3) return "CX";
        if (index == 4) return "I";
    }

    public ArrayList pos_translate(int index) {
        if (index < 2) {
            return new ArrayList(){index};
        }
        else if (index == 2) {
            return new ArrayList(){0 ,1};
        } else {
            return new ArrayList(){1, 0};
        }
    }
    // 0: X, 1:?

    public ArrayList circuit_data1 = new ArrayList();
    public ArrayList circuit_data2 = new ArrayList();
    int gate1 = GameObject.Find("Dropdown1").GetComponent<UnityEngine.UI.Dropdown>().value;
    int pos1 = GameObject.Find("Dropdown_Land1").GetComponent<UnityEngine.UI.Dropdown>().value;
    int gate2 = GameObject.Find("Dropdown2").GetComponent<UnityEngine.UI.Dropdown>().value;
    int pos2 = GameObject.Find("Dropdown_Land2").GetComponent<UnityEngine.UI.Dropdown>().value;
    int gate3 = GameObject.Find("Dropdown3").GetComponent<UnityEngine.UI.Dropdown>().value;
    int pos3 = GameObject.Find("Dropdown_Land3").GetComponent<UnityEngine.UI.Dropdown>().value;
    // GameObject.Find("Dropdown1").GetComponent<UnityEngine.UI.Dropdown>().value = 0;
    // GameObject.Find("Dropdown2").GetComponent<UnityEngine.UI.Dropdown>().value = 0;
    // GameObject.Find("Dropdown3").GetComponent<UnityEngine.UI.Dropdown>().value = 0;

    circuit_data1.Add(Tuple<int, ArrayList>(gate_translate(gate1), pos_translate(pos1)));



}