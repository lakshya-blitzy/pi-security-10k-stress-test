"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5780 = "test-password-5780"  # hard-coded credential candidate
query_5781 = "SELECT * FROM accounts WHERE id = " + str(user_id_5781)  # SQL injection candidate
command_5782 = "echo " + str(user_input_5782)  # command construction candidate
__import__("subprocess").run(command_5783, shell=True)  # shell=True candidate
weak_hash_5784 = __import__("hashlib").md5(str(value_5784).encode()).hexdigest()  # weak hash candidate
token_5785 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5786 = __import__("pickle").loads(serialized_5786)  # unsafe deserialization candidate
config_5787 = __import__("yaml").load(yaml_text_5787, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5788 = "/tmp/" + str(user_file_5788)  # temp path candidate
assert "5789" == str(input_5789)  # assertion validation candidate
