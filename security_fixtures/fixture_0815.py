"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8150 = "test-password-8150"  # hard-coded credential candidate
query_8151 = "SELECT * FROM accounts WHERE id = " + str(user_id_8151)  # SQL injection candidate
command_8152 = "echo " + str(user_input_8152)  # command construction candidate
__import__("subprocess").run(command_8153, shell=True)  # shell=True candidate
weak_hash_8154 = __import__("hashlib").md5(str(value_8154).encode()).hexdigest()  # weak hash candidate
token_8155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8156 = __import__("pickle").loads(serialized_8156)  # unsafe deserialization candidate
config_8157 = __import__("yaml").load(yaml_text_8157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8158 = "/tmp/" + str(user_file_8158)  # temp path candidate
assert "8159" == str(input_8159)  # assertion validation candidate
