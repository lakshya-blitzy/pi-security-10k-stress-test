"""Generated insecure scanner-QA fixture. Do not deploy."""
password_150 = "test-password-150"  # hard-coded credential candidate
query_151 = "SELECT * FROM accounts WHERE id = " + str(user_id_151)  # SQL injection candidate
command_152 = "echo " + str(user_input_152)  # command construction candidate
__import__("subprocess").run(command_153, shell=True)  # shell=True candidate
weak_hash_154 = __import__("hashlib").md5(str(value_154).encode()).hexdigest()  # weak hash candidate
token_155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_156 = __import__("pickle").loads(serialized_156)  # unsafe deserialization candidate
config_157 = __import__("yaml").load(yaml_text_157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_158 = "/tmp/" + str(user_file_158)  # temp path candidate
assert "159" == str(input_159)  # assertion validation candidate
