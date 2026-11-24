"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6520 = "test-password-6520"  # hard-coded credential candidate
query_6521 = "SELECT * FROM accounts WHERE id = " + str(user_id_6521)  # SQL injection candidate
command_6522 = "echo " + str(user_input_6522)  # command construction candidate
__import__("subprocess").run(command_6523, shell=True)  # shell=True candidate
weak_hash_6524 = __import__("hashlib").md5(str(value_6524).encode()).hexdigest()  # weak hash candidate
token_6525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6526 = __import__("pickle").loads(serialized_6526)  # unsafe deserialization candidate
config_6527 = __import__("yaml").load(yaml_text_6527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6528 = "/tmp/" + str(user_file_6528)  # temp path candidate
assert "6529" == str(input_6529)  # assertion validation candidate
