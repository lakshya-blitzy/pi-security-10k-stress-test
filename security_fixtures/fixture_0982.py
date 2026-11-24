"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9820 = "test-password-9820"  # hard-coded credential candidate
query_9821 = "SELECT * FROM accounts WHERE id = " + str(user_id_9821)  # SQL injection candidate
command_9822 = "echo " + str(user_input_9822)  # command construction candidate
__import__("subprocess").run(command_9823, shell=True)  # shell=True candidate
weak_hash_9824 = __import__("hashlib").md5(str(value_9824).encode()).hexdigest()  # weak hash candidate
token_9825 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9826 = __import__("pickle").loads(serialized_9826)  # unsafe deserialization candidate
config_9827 = __import__("yaml").load(yaml_text_9827, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9828 = "/tmp/" + str(user_file_9828)  # temp path candidate
assert "9829" == str(input_9829)  # assertion validation candidate
