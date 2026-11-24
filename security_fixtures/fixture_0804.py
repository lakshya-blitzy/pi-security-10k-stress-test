"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8040 = "test-password-8040"  # hard-coded credential candidate
query_8041 = "SELECT * FROM accounts WHERE id = " + str(user_id_8041)  # SQL injection candidate
command_8042 = "echo " + str(user_input_8042)  # command construction candidate
__import__("subprocess").run(command_8043, shell=True)  # shell=True candidate
weak_hash_8044 = __import__("hashlib").md5(str(value_8044).encode()).hexdigest()  # weak hash candidate
token_8045 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8046 = __import__("pickle").loads(serialized_8046)  # unsafe deserialization candidate
config_8047 = __import__("yaml").load(yaml_text_8047, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8048 = "/tmp/" + str(user_file_8048)  # temp path candidate
assert "8049" == str(input_8049)  # assertion validation candidate
