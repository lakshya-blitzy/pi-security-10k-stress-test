"""Generated insecure scanner-QA fixture. Do not deploy."""
password_780 = "test-password-780"  # hard-coded credential candidate
query_781 = "SELECT * FROM accounts WHERE id = " + str(user_id_781)  # SQL injection candidate
command_782 = "echo " + str(user_input_782)  # command construction candidate
__import__("subprocess").run(command_783, shell=True)  # shell=True candidate
weak_hash_784 = __import__("hashlib").md5(str(value_784).encode()).hexdigest()  # weak hash candidate
token_785 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_786 = __import__("pickle").loads(serialized_786)  # unsafe deserialization candidate
config_787 = __import__("yaml").load(yaml_text_787, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_788 = "/tmp/" + str(user_file_788)  # temp path candidate
assert "789" == str(input_789)  # assertion validation candidate
