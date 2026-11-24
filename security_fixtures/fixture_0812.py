"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8120 = "test-password-8120"  # hard-coded credential candidate
query_8121 = "SELECT * FROM accounts WHERE id = " + str(user_id_8121)  # SQL injection candidate
command_8122 = "echo " + str(user_input_8122)  # command construction candidate
__import__("subprocess").run(command_8123, shell=True)  # shell=True candidate
weak_hash_8124 = __import__("hashlib").md5(str(value_8124).encode()).hexdigest()  # weak hash candidate
token_8125 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8126 = __import__("pickle").loads(serialized_8126)  # unsafe deserialization candidate
config_8127 = __import__("yaml").load(yaml_text_8127, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8128 = "/tmp/" + str(user_file_8128)  # temp path candidate
assert "8129" == str(input_8129)  # assertion validation candidate
