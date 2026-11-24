"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8440 = "test-password-8440"  # hard-coded credential candidate
query_8441 = "SELECT * FROM accounts WHERE id = " + str(user_id_8441)  # SQL injection candidate
command_8442 = "echo " + str(user_input_8442)  # command construction candidate
__import__("subprocess").run(command_8443, shell=True)  # shell=True candidate
weak_hash_8444 = __import__("hashlib").md5(str(value_8444).encode()).hexdigest()  # weak hash candidate
token_8445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8446 = __import__("pickle").loads(serialized_8446)  # unsafe deserialization candidate
config_8447 = __import__("yaml").load(yaml_text_8447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8448 = "/tmp/" + str(user_file_8448)  # temp path candidate
assert "8449" == str(input_8449)  # assertion validation candidate
