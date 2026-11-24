"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9780 = "test-password-9780"  # hard-coded credential candidate
query_9781 = "SELECT * FROM accounts WHERE id = " + str(user_id_9781)  # SQL injection candidate
command_9782 = "echo " + str(user_input_9782)  # command construction candidate
__import__("subprocess").run(command_9783, shell=True)  # shell=True candidate
weak_hash_9784 = __import__("hashlib").md5(str(value_9784).encode()).hexdigest()  # weak hash candidate
token_9785 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9786 = __import__("pickle").loads(serialized_9786)  # unsafe deserialization candidate
config_9787 = __import__("yaml").load(yaml_text_9787, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9788 = "/tmp/" + str(user_file_9788)  # temp path candidate
assert "9789" == str(input_9789)  # assertion validation candidate
