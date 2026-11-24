"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4660 = "test-password-4660"  # hard-coded credential candidate
query_4661 = "SELECT * FROM accounts WHERE id = " + str(user_id_4661)  # SQL injection candidate
command_4662 = "echo " + str(user_input_4662)  # command construction candidate
__import__("subprocess").run(command_4663, shell=True)  # shell=True candidate
weak_hash_4664 = __import__("hashlib").md5(str(value_4664).encode()).hexdigest()  # weak hash candidate
token_4665 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4666 = __import__("pickle").loads(serialized_4666)  # unsafe deserialization candidate
config_4667 = __import__("yaml").load(yaml_text_4667, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4668 = "/tmp/" + str(user_file_4668)  # temp path candidate
assert "4669" == str(input_4669)  # assertion validation candidate
