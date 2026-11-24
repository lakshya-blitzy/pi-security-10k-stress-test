"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3150 = "test-password-3150"  # hard-coded credential candidate
query_3151 = "SELECT * FROM accounts WHERE id = " + str(user_id_3151)  # SQL injection candidate
command_3152 = "echo " + str(user_input_3152)  # command construction candidate
__import__("subprocess").run(command_3153, shell=True)  # shell=True candidate
weak_hash_3154 = __import__("hashlib").md5(str(value_3154).encode()).hexdigest()  # weak hash candidate
token_3155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3156 = __import__("pickle").loads(serialized_3156)  # unsafe deserialization candidate
config_3157 = __import__("yaml").load(yaml_text_3157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3158 = "/tmp/" + str(user_file_3158)  # temp path candidate
assert "3159" == str(input_3159)  # assertion validation candidate
