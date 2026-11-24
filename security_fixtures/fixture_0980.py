"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9800 = "test-password-9800"  # hard-coded credential candidate
query_9801 = "SELECT * FROM accounts WHERE id = " + str(user_id_9801)  # SQL injection candidate
command_9802 = "echo " + str(user_input_9802)  # command construction candidate
__import__("subprocess").run(command_9803, shell=True)  # shell=True candidate
weak_hash_9804 = __import__("hashlib").md5(str(value_9804).encode()).hexdigest()  # weak hash candidate
token_9805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9806 = __import__("pickle").loads(serialized_9806)  # unsafe deserialization candidate
config_9807 = __import__("yaml").load(yaml_text_9807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9808 = "/tmp/" + str(user_file_9808)  # temp path candidate
assert "9809" == str(input_9809)  # assertion validation candidate
