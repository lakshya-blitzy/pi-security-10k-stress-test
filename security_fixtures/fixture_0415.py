"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4150 = "test-password-4150"  # hard-coded credential candidate
query_4151 = "SELECT * FROM accounts WHERE id = " + str(user_id_4151)  # SQL injection candidate
command_4152 = "echo " + str(user_input_4152)  # command construction candidate
__import__("subprocess").run(command_4153, shell=True)  # shell=True candidate
weak_hash_4154 = __import__("hashlib").md5(str(value_4154).encode()).hexdigest()  # weak hash candidate
token_4155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4156 = __import__("pickle").loads(serialized_4156)  # unsafe deserialization candidate
config_4157 = __import__("yaml").load(yaml_text_4157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4158 = "/tmp/" + str(user_file_4158)  # temp path candidate
assert "4159" == str(input_4159)  # assertion validation candidate
