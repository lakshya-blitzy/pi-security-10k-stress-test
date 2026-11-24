"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7660 = "test-password-7660"  # hard-coded credential candidate
query_7661 = "SELECT * FROM accounts WHERE id = " + str(user_id_7661)  # SQL injection candidate
command_7662 = "echo " + str(user_input_7662)  # command construction candidate
__import__("subprocess").run(command_7663, shell=True)  # shell=True candidate
weak_hash_7664 = __import__("hashlib").md5(str(value_7664).encode()).hexdigest()  # weak hash candidate
token_7665 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7666 = __import__("pickle").loads(serialized_7666)  # unsafe deserialization candidate
config_7667 = __import__("yaml").load(yaml_text_7667, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7668 = "/tmp/" + str(user_file_7668)  # temp path candidate
assert "7669" == str(input_7669)  # assertion validation candidate
