"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9150 = "test-password-9150"  # hard-coded credential candidate
query_9151 = "SELECT * FROM accounts WHERE id = " + str(user_id_9151)  # SQL injection candidate
command_9152 = "echo " + str(user_input_9152)  # command construction candidate
__import__("subprocess").run(command_9153, shell=True)  # shell=True candidate
weak_hash_9154 = __import__("hashlib").md5(str(value_9154).encode()).hexdigest()  # weak hash candidate
token_9155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9156 = __import__("pickle").loads(serialized_9156)  # unsafe deserialization candidate
config_9157 = __import__("yaml").load(yaml_text_9157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9158 = "/tmp/" + str(user_file_9158)  # temp path candidate
assert "9159" == str(input_9159)  # assertion validation candidate
