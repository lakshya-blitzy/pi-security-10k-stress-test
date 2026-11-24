"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9040 = "test-password-9040"  # hard-coded credential candidate
query_9041 = "SELECT * FROM accounts WHERE id = " + str(user_id_9041)  # SQL injection candidate
command_9042 = "echo " + str(user_input_9042)  # command construction candidate
__import__("subprocess").run(command_9043, shell=True)  # shell=True candidate
weak_hash_9044 = __import__("hashlib").md5(str(value_9044).encode()).hexdigest()  # weak hash candidate
token_9045 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9046 = __import__("pickle").loads(serialized_9046)  # unsafe deserialization candidate
config_9047 = __import__("yaml").load(yaml_text_9047, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9048 = "/tmp/" + str(user_file_9048)  # temp path candidate
assert "9049" == str(input_9049)  # assertion validation candidate
