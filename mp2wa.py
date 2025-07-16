import os
import subprocess
from pydub import AudioSegment

def convert_mp3_to_wav(input_mp3, output_wav=None):
    """综合解决方案，尝试多种方法转换MP3到WAV"""
    if output_wav is None:
        output_wav = os.path.splitext(input_mp3)[0] + ".wav"
    
    # 方法1: 首先尝试标准pydub方法
    try:
        audio = AudioSegment.from_mp3(input_mp3)
        audio.export(output_wav, format="wav")
        print("使用标准方法转换成功")
        return True
    except:
        pass
    
    # 方法2: 尝试原始文件读取
    try:
        audio = AudioSegment.from_file(input_mp3, format="mp3")
        audio.export(output_wav, format="wav")
        print("使用原始文件读取方法转换成功")
        return True
    except:
        pass
    
    # 方法3: 使用FFmpeg直接转换
    try:
        ffmpeg_convert(input_mp3, output_wav)
        print("使用FFmpeg直接转换成功")
        return True
    except:
        pass
    
    # 方法4: 尝试修复文件后转换
    try:
        fixed_file = "fixed_" + os.path.basename(input_mp3)
        if try_fix_mp3(input_mp3, fixed_file):
            return convert_mp3_to_wav(fixed_file, output_wav)
    except:
        pass
    
    print("所有转换方法均失败")
    return False

if __name__ == "__main__":
    input_file = input("请输入MP3文件路径: ").strip('"')
    if os.path.exists(input_file) and input_file.lower().endswith('.mp3'):
        convert_mp3_to_wav(input_file)
    else:
        print("错误: 文件不存在或不是MP3格式")