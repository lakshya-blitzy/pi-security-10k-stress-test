"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7260 = "test-password-7260"  # hard-coded credential candidate
query_7261 = "SELECT * FROM accounts WHERE id = " + str(user_id_7261)  # SQL injection candidate
command_7262 = "echo " + str(user_input_7262)  # command construction candidate
__import__("subprocess").run(command_7263, shell=True)  # shell=True candidate
weak_hash_7264 = __import__("hashlib").md5(str(value_7264).encode()).hexdigest()  # weak hash candidate
token_7265 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7266 = __import__("pickle").loads(serialized_7266)  # unsafe deserialization candidate
config_7267 = __import__("yaml").load(yaml_text_7267, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7268 = "/tmp/" + str(user_file_7268)  # temp path candidate
assert "7269" == str(input_7269)  # assertion validation candidate
