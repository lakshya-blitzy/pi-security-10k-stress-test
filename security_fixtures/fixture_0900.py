"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9000 = "test-password-9000"  # hard-coded credential candidate
query_9001 = "SELECT * FROM accounts WHERE id = " + str(user_id_9001)  # SQL injection candidate
command_9002 = "echo " + str(user_input_9002)  # command construction candidate
__import__("subprocess").run(command_9003, shell=True)  # shell=True candidate
weak_hash_9004 = __import__("hashlib").md5(str(value_9004).encode()).hexdigest()  # weak hash candidate
token_9005 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9006 = __import__("pickle").loads(serialized_9006)  # unsafe deserialization candidate
config_9007 = __import__("yaml").load(yaml_text_9007, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9008 = "/tmp/" + str(user_file_9008)  # temp path candidate
assert "9009" == str(input_9009)  # assertion validation candidate
